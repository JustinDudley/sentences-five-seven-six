const fs = require('fs');

const data = fs.readFileSync('./groups-input.json', 'utf-8');
const sentences = JSON.parse(data)

// 1. convert "group" property from string to array
const sentencesGroupHasNoSpaces = []
sentences.forEach(sentence => {
    const groupNoSpaces = sentence.group.replace(/\s/g, '')
    delete sentence.group;
    sentence.group = groupNoSpaces
    sentencesGroupHasNoSpaces.push(sentence)
})

const sentencesGroupIsAnArray = []
sentences.forEach(sentence => {
    const groupArr = sentence.group.split(',')
    delete sentence.group;
    sentence.group = groupArr
    sentencesGroupIsAnArray.push(sentence)
})
// NOW I have a good array of sentences, called sentencesGroupIsAnArray


// 2. 




const finalSentences = []

// for (const outerSentence of sentencesGroupIsAnArray) {

sentencesGroupIsAnArray.forEach(outerSentence => {

    if (outerSentence.letter_pair === "BC") {
        let biggerGroup = [];
        sentencesGroupIsAnArray.forEach(innerSentence => {
            if(innerSentence.group.includes('bc')) {
                console.log('innerSentence is: ', innerSentence)
                biggerGroup.push.apply(biggerGroup, innerSentence.group)
                biggerGroup = [...new Set(biggerGroup)];

            }
        })

        delete outerSentence.group;
        outerSentence.group = biggerGroup
        finalSentences.push(outerSentence)
    }
});

console.log(finalSentences[0])