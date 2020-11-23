const textArea = document.getElementById('input')
const positiveScoreBar = document.getElementById('positive-sentiment-bar-fill')
const emoji = document.getElementById('emoji')

const apiBaseUrl = 'http://localhost:4242'

const happyEmoji = '😀'
const neutralEmoji = '😐'
const angeryEmoji = '😠'

const percentage = (value, sum) => (value / sum) * 100

const updateSentimentScore = (pos) => {
    positiveScoreBar.style.width = `${pos}%`
}

const updateEmoji = (pos) => {
    if (pos > 65) {
        emoji.innerText = happyEmoji
    } else if (pos < 45) {
        emoji.innerText = angeryEmoji
    } else {
        emoji.innerText = neutralEmoji
    }
}

const getPrediction = async (text) => {
    const response = await fetch(`${apiBaseUrl}/api/predict?sample=${text}`, { method: 'POST' })
    const body = await response.json()
    return body.prediction
}

const getSentiment = async () => {
    const text = textArea.value
    const { positive, negative } = await getPrediction(text)
    if (positive == null) return
    const total = positive + negative

    const posPercentage = percentage(positive, total)

    updateSentimentScore(posPercentage)
    updateEmoji(posPercentage)
}