#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
  ifstream inFS1, inFS2;
  string file1, file2;
  cout << "Enter the first file to compare: ";
  cin >> file1;
  cout << "Enter the second file to compare: ";
  cin >> file2;
  
  inFS1.open(file1.c_str());
  inFS2.open(file2.c_str());

  if(!inFS1.is_open()) {
    cout << "Could not open \"" << file1 << "\"" << endl;
    return -1;
  }
  if(!inFS2.is_open()) {
    cout << "Could not open \"" << file2 << "\"" << endl;
    return -2;
  }

  string p31, p32;
  inFS1 >> p31;
  inFS2 >> p32;
  if(p31 != p32) {
    cout << "File types don't match" << endl;
    return -3;
  }

  int width1, height1, width2, height2;
  inFS1 >> width1 >> height1;
  inFS2 >> width2 >> height2;
  if(width1 != width2) {
    cout << "widths don't match" << endl;
    return -4;
  }
  if(height1 != height2) {
    cout << "heights don't match" << endl;
    return -5;
  }

  int maxVal1, maxVal2;
  inFS1 >> maxVal1;
  inFS2 >> maxVal2;
  if(maxVal1 != maxVal2) {
    cout << "max vals don't match" << endl;
    return -6;
  }

  for(int i = 0; i < height1; i++) {
    for(int j = 0; j < width1; j++) {
      int r1, g1, b1, r2, g2, b2;
      inFS1 >> r1 >> g1 >> b1;
      inFS2 >> r2 >> g2 >> b2;
      if(r1 != r2) {
        cout << "pixel (" << i << ", " << j << ") red doesn't match" << endl;
        return -7;
      }
      if(g1 != g2) {
        cout << "pixel (" << i << ", " << j << ") green doesn't match" << endl;
        return -8;
      }
      if(b1 != b2) {
        cout << "pixel (" << i << ", " << j << ") blue doesn't match" << endl;
        return -9;
      }
    }
  }

  cout << "Images match" << endl;

  return 0;
}
