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


// 2. Create finalSentences array
const finalSentences = []

sentencesGroupIsAnArray.forEach(outerSentence => {
    let biggerGroup = [];
    sentencesGroupIsAnArray.forEach(innerSentence => {
        if(innerSentence.group.includes(outerSentence.letter_pair.toLowerCase())) {
            biggerGroup.push.apply(biggerGroup, innerSentence.group)
            biggerGroup = [...new Set(biggerGroup)];
        }
    })
    finalSentences.push({letter_pair: outerSentence.letter_pair, group: biggerGroup})
      
});


// write finalSentences to file
fs.writeFile('groups-output.json', JSON.stringify(finalSentences), function (err) {
    if (err) throw err;
    console.log('Saved!');
  });