// Purpose:
// To add all known associations of a given letter_pair to the group for that letter_pair.
// So:  We look at letter_pair YQ.  Who is yq known to associate with?  That is, in what groups is yq found?
// collect all the letter_pairs with which yq is found.  Remove duplicates. Add this list of letter_pairs to the group for yq

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
const almostFinalSentences = []

sentencesGroupIsAnArray.forEach(outerSentence => {
    let biggerGroup = [];
    sentencesGroupIsAnArray.forEach(innerSentence => {
        if(innerSentence.group.includes(outerSentence.letter_pair.toLowerCase())) {
            biggerGroup.push.apply(biggerGroup, innerSentence.group)
            biggerGroup = [...new Set(biggerGroup)];
        }
    })
    almostFinalSentences.push({letter_pair: outerSentence.letter_pair, group: biggerGroup})
      
});


// 3. convert group property BACK to string (from array)
finalSentences = []
almostFinalSentences.forEach(sentence => {
    const localGroup = sentence.group.join(', ')
    finalSentences.push({letter_pair: sentence.letter_pair, group: localGroup})
})


// 4. write finalSentences to file
fs.writeFile('groups-output.json', JSON.stringify(finalSentences), function (err) {
    if (err) throw err;
    console.log('Saved!');
  });