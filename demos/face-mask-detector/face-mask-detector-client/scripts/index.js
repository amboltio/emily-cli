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
  image = image.slice(22)
  const data = new FormData()
  data.append('sample', image)
  
  return data
}

const handleEmilyPrediction = (result) => {
  prediction = result.prediction
  return prediction == 0 ? false : prediction == 1 ? true : prediction
}

const getPrediction = async (image) => {
  data = prepareImage(image)
  console.log(data)
  
  const result = await fetch('http://localhost:4242/api/predict', {
    method: 'POST',
    body: data
  })

  return handleEmilyPrediction(await result.json())
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
  }
}


startWebcam() 
  .then(async () => {
    await beginDetectionLoop()
  })
