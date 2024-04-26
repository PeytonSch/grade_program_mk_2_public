#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#include "functions.h"

int main() {
    // open file for parsing
    string filename = promptUserForFilename();
    ifstream fileIn;
    if( !openFile(fileIn, filename) ) {
        cerr << "Could not open file \"" << filename << "\"" << endl;
        cerr << "Shutting down" << endl;
        return -1;
    }

    // read all the words in the file
    vector<string> allWords = readWordsFromFile( fileIn );
    fileIn.close();
    cout << "Read in " << allWords.size() << " words" << endl;

    // clean the words to remove punctuation and convert to uppercase
    removePunctuation(allWords, "?!.,;:\"()_");
    capitalizeWords(allWords);

    // find only the unique words in the file
    vector<string> uniqueWords = filterUniqueWords(allWords);
    cout << "Encountered " << uniqueWords.size() << " unique words" << endl;

    // put the words in to alphabetical order
    alphabetizeWords( uniqueWords );

    // count the number of occurrences of each word
    vector<unsigned int> uniqueWordCounts = countUniqueWords(allWords, uniqueWords);

    // pretty print the unique words and their corresponding counts
    printWordsAndCounts(uniqueWords, uniqueWordCounts);

    // count the occurrences of every letter in the entire text
    unsigned int letters[26] = {0};
    countLetters(letters, allWords);
    printLetterCounts(letters);

    // print statistics on word and letter frequencies
    printMaxMinWord(uniqueWords, uniqueWordCounts);
    printMaxMinLetter(letters);


    return 0;
}