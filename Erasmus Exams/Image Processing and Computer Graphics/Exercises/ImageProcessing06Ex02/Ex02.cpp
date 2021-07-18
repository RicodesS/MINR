/**
 * Image Processing and Computer Graphics
 *
 * Exercise 2: Motion estimation
 */

#include <cstdlib>   /// contains: EXIT_SUCCESS
#include <iostream>  /// contains: std::cout etc.
#include "CMatrix.h"

int main(int argc, char** args) 
{  
  /// Tell the compiler not to throw warnings for unused variables
  /// Remove these lines if you want to use command line arguments.
  (void)argc;
  (void)args;

  /// Print something so we know the program actually runs
  std::cout << "Hello, World!\n";

  /**
   * EXERCISE 2: Implement the Lucas-Kanade method for optical flow 
   * estimation. 
   * For your convenience, make use of the convolution function 
   * NFilter::filter and the predefined filter masks CSmooth and 
   * CDerivative in CFilter.h. 
   * Try your implementation with the Street sequence. 
   * For visualization you can make use of the function flowToImage.
   * Adjust the size of the Gaussian neighborhood and play with 
   * this parameter.
   * Presmooth the input images before computing the gradients. 
   * Play with the amount of smoothing.
   **/

  CMatrix<float> frame1;
  CMatrix<float> frame2;
  frame1.readFromPGM("cropped-street_000009.pgm");
  frame2.readFromPGM("cropped-street_000010.pgm");
  

  return EXIT_SUCCESS;
}

