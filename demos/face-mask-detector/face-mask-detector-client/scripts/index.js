const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas');
const snapSoundElement = document.getElementById('snapSound');
const webcam = new Webcam(webcamElement, 'user', canvasElement, snapSoundElement);

const [loadingIcon] = document.getElementsByClassName('loading-icon')
const [statusMessage] = document.getElementsByClassName('status')
const [webcamFeed] = document.getElementsByClassName('webcam-feed')

const startWebcam = async () => {
    try {
        await webcam.start()
        console.log('Webcam started')
    } catch (err) {
        console.error(err)
    }
}

const prepareImage = (image) => {

    // Remove first 22 chars from string as they are meta info
    image = image.slice(22)
    return image
}

const getPrediction = async (image) => {

    image = prepareImage(image)

    // Send POST request
    const response = await fetch('http://localhost:4242/api/predict-webcam', {
        method: 'POST',
        body: JSON.stringify({"image": image, "model_path": "data/models/resnet_18_epoch_153_acc_93.53.pth"})
    })
    const responseBody = await response.json()

    console.log("Prediction: " + responseBody.prediction)
    return responseBody.prediction >= 50
}

const beginDetectionLoop = async () => {
    const picture = webcam.snap()
    console.log(picture)

    while (true) {

        const picture = webcam.snap()
        const hasMask = await getPrediction(picture);
        console.log(`Got prediction for has mask: ${hasMask}`)

        if (hasMask == null)
            continue

        loadingIcon.classList.add('disabled')
        if (hasMask) {
            webcamFeed.classList.remove('warn')
            statusMessage.classList.remove('warn')
            webcamFeed.classList.add('success')
            statusMessage.classList.add('success')

            statusMessage.innerHTML = '✓ Mask found!'
        } else {
            webcamFeed.classList.remove('success')
            statusMessage.classList.remove('success')
            webcamFeed.classList.add('warn')
            statusMessage.classList.add('warn')
            statusMessage.innerHTML = '✗ No mask found'
        }

        // Set sleep timeout for 1/3 of a sec to avoid the CPU/GPU to be overflown with requests
        await new Promise(r => setTimeout(r, 333));
    }
}


startWebcam()
    .then(async () => {
        await beginDetectionLoop()
    })
