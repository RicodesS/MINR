/**
 * Image Processing and Computer Graphics
 *
 * Exercise 1: Noise, basic operators and filters
 * 
 * Author: Riccardo Salvalaggio
 */

#include <cstdlib>   /// contains: EXIT_SUCCESS
#include <iostream>  /// contains: std::cout etc.
#include "CMatrix.h"
#include <iomanip>
#include <string>
#include <map>
#include <random>
#include <cmath>

int main(int argc, char** args) 
{  
  /// Tell the compiler not to throw warnings for unused variables
  /// Remove these lines if you want to use command line arguments.
  (void)argc;
  (void)args;


  /// Print something so we know the program actually runs
  std::cout << "Hello, World!\n";

  /// Define image
  CMatrix<float> aImage;
  /// Read image from a PGM file
  aImage.readFromPGM("sunset.pgm");
  /// Add Gaussian noise here

  for (int y = 0; y < aImage.ySize(); ++y) {
    for (int x = 0; x < aImage.xSize(); ++x) {
        float U = rand() % 100;
        U = U/100;
        float V = rand() % 100;
        V = V /100;

        //std::cout << "U: "<< U;
        //std::cout << '\n';
        //std::cout << "V: "<< V;
        //std::cout << '\n';
        float N = sqrt(-2*log(U))*cos(6.28*V);

        //std::cout << "N: "<< N;
        //std::cout << '\n';

        aImage(x,y) += N;
    }
  }
  /// Write noisy image to PGM file
  aImage.writeToPGM("sunsetNoisy.pgm");      

  CTensor<float> sImage = new CTensor<float>::CTensor();
  CTensor<float> bgImage = new CTensor<float>::CTensor();
  CTensor<float> dImage = new CTensor<float>::CTensor();


  sImage.readFromPPM("Sidenbladh.ppm");
  dImage.readFromPPM("Sidenbladh.ppm");
  bgImage.readFromPPM("SidenbladhBG.ppm");

  for (int y = 0; y < sImage.ySize(); ++y) {
    for (int x = 0; x < sImage.xSize(); ++x) {
      dImage(x,y) = sImage(x,y) - bgImage(x,y);
    }
  }
  dImage.writeToPPM("difference.ppm");      

  return EXIT_SUCCESS;

}

