const textArea = document.getElementById('input')
const emoji = document.getElementById('emoji')
const costumerAnwser = document.getElementById('costumerAnwser')

const apiBaseUrl = 'http://localhost:4242'

emoji.innerText = '🍕'
costumerAnwser.innerText = 'Hej jeg vil gerne bestille en pizza'

Array.prototype.random = function () {
    return this[Math.floor((Math.random()*this.length))];
  }

const getPrediction = async (text) => {
    const response = await fetch(`${apiBaseUrl}/api/predict?sample=${text}&model_path=emily/model`, { method: 'POST' })
    const body = await response.json()
    return body
}

const getAwnser = async (e) => {
    if (e.keyCode == 13){
        const text = textArea.value
        textArea.value = ""
        const prediction = await getPrediction(text)
        if (prediction['result'] != null){
            costumerAnwser.innerText = prediction['result']['response']
        } else {
            costumerAnwser.innerText = 'Undskyld det forstod jeg ikke'
        }
    }
}
