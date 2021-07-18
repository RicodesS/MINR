/**
 * @author Nikolaus Mayer, 2015 (mayern@cs.uni-freiburg.de)
 *
 * @brief Image Processing and Computer Graphics
 *        Winter Term 2015/2016
 *        Exercise Sheet 1 (Image Processing part)
 */

/// STL/System
#include <algorithm>  /// max, min
#include <cmath>      /// sqrt, sin, cos, log, log10, exp
#include <cstdlib>    /// srand, rand, EXIT_SUCCESS
#include <ctime>      /// time
#include <iostream>   /// cout
#include <stdexcept>  /// runtime_error
#include <vector>     /// vector<T>
/// Local files
#include "CMatrix.h"
#include "CTensor.h"
#include "ImageDisplay.h"


const float PI = 3.14159265358979323846f;


ImageDisplay::ImageDisplay* disp{nullptr};


/**
 * @brief Sample a 1d normal distribution (C++11 version)
 *
 * @param initial_mu Mean of the distribution, set on first function
 *                   call
 * @param initial_sigma Standard deviation of the distribution, set on
 *                      first function call
 *
 * @returns A random number sampled from a normal distribution with
 *          (mean=initial_mu, sigma=initial_sigma)
 */
// float random_number_new(float initial_mu=-1.f, 
//                         float initial_sigma=-1.f)
// {
//   /// http://en.cppreference.com/w/cpp/numeric/random/normal_distribution
//   static std::random_device rd;
//   static std::mt19937 gen{rd()};
//   static std::normal_distribution<float> RNG(initial_mu, initial_sigma);

//   return RNG(gen);
// }


/**
 * @brief Sample a 1d normal distribution (old C++ [=C++98/03] version)
 *        using the Box-Muller method 
 *        (https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform)
 *
 * @param initial_mu Mean of the distribution, set on first function
 *                   call
 * @param initial_sigma Standard deviation of the distribution, set on
 *                      first function call
 *
 * @returns A random number sampled from a normal distribution with
 *          (mean=initial_mu, sigma=initial_sigma)
 */
float random_number_old(float initial_mu=-1.f, 
                        float initial_sigma=-1.f)
{
  /// On first call, seed pseudo random number generator using current
  /// system time
  static bool initialized=false;
  static float mu;
  static float sigma;
  if (not initialized) {
    std::srand(std::time(0));
    mu = initial_mu;
    sigma = initial_sigma;
    initialized = true;
  }

  /// Generate two uniform samples from [0,1]
  double U = std::rand() / ((double) RAND_MAX);
  double V = std::rand() / ((double) RAND_MAX);
  /// Transform into normal distribution arount mu=0
  float N = std::sqrt(-2*sigma*sigma*std::log(U))*std::cos(2*PI*V);
  /// The Box-Muller method can yield two numbers, but we only need one
  //float M = sqrt(-2*sigma*sigma*log(U))*sin(2*PI*V);

  /// Add mean and return
  return N + mu;
}


/**
 * @brief Add Gaussian distributed pixel noise to an image
 *
 * @param image The image
 * @param sigma Standard deviation of the noise
 * @param clamp IFF TRUE, restrict result values to [0,255]
 */
void AddGaussianNoise(CMatrix<float>& image,
                      float sigma,
                      bool clamp)
{
  for ( int y = 0; y < image.ySize(); ++y ) {
    for ( int x = 0; x < image.xSize(); ++x ) {
      /// Add noise to pixel
      float& pixel = image(x,y);
      // pixel += random_number_new(0.f, sigma);
      pixel += random_number_old(0.f, sigma);
      /// Clamp pixel value to [0,255]
      if (clamp) {
        pixel = std::max(0.f, std::min(pixel, 255.f));
      }
    }
  }
}


/**
 * @brief Square a number
 *
 * @param a Number to be squared
 *
 * @returns Square of the input
 */
template <typename T>
inline T square(T a)
{ 
  return a*a; 
}


/**
 * @brief Compute peak signal-to-noise ratio of an image, given a 
 *        noise-free reference image
 *
 * @param ground_truth Noise-free image
 * @param noisy_sample Noisy version of the "ground_truth" image
 *
 * @returns PSNR in decibels (dB)
 */
float PSNR(const CMatrix<float>& ground_truth,
            CMatrix<float>& noisy_sample)
{
  /// Variance of the noise 
  float noise_sigma_square = 0.;
  for ( int y = 0; y < ground_truth.ySize(); ++y ) {
    for ( int x = 0; x < ground_truth.xSize(); ++x ) {
      noise_sigma_square += square(ground_truth(x,y) - noisy_sample(x,y));
    }
  }

  /// PSNR
  size_t N = ground_truth.xSize() * ground_truth.ySize();
  float range = ground_truth.max()-ground_truth.min();
  float PSNR = 10.f*std::log10((N*square(range))/noise_sigma_square);

  return PSNR;
}



/**
 * @brief Part 1: Additive Gaussian noise
 */
void Ex01_a_GaussianNoise() 
{
  std::cout << "----- Additive Gaussian noise -----\n";
  float sigma = 0.f;
  do {
    std::cout << "Choose variance (>= 0): ";
    std::cin >> sigma;
  } while (sigma < 0.f);
  std::cout << "Noising Sunset with standard deviation " << sigma 
            << " ...\n";
  
  /// Read image from a PGM file
  CMatrix<float> aImage;
  aImage.readFromPGM("sunset.pgm");
  disp->Display(aImage, "Additive Gaussian noise (original image)");
  /// Add noise
  AddGaussianNoise(aImage, sigma, true);
  /// Write noisy image to PGM file
  aImage.writeToPGM("sunsetNoisy.pgm");
  disp->Display(aImage, "Additive Gaussian noise (noisy image)");
}


/**
 * @brief Clamp pixel values of an image to [0,255]
 *
 * @param image Input image
 *
 * @returns The input image with each pixel within [0,255]
 */
CMatrix<float> Clamp(const CMatrix<float>& image)
{
  CMatrix<float> result(image);
  for (int y = 0; y < result.ySize(); ++y) {
    for (int x = 0; x < result.xSize(); ++x) {
      result(x,y) = std::max(0.f, std::min(result(x,y), 255.f));
    }
  }
  return result;
}


/**
 * @brief Part 2: PSNR
 */
void Ex01_b_PSNR() 
{
  std::cout << "----- PSNR -----\n";
  float sigma = 0.f;
  do {
    std::cout << "Choose variance (>= 0): ";
    std::cin >> sigma;
  } while (sigma < 0.f);
  int number_of_samples = 0;
  do {
    std::cout << "Choose number of samples (>= 1): ";
    std::cin >> number_of_samples;
  } while (number_of_samples < 1);
  std::cout << "Creating " << number_of_samples
            << " noisy images (stddev=" << sigma << ")...\n";
  int display_every = 0;
  do {
    std::cout << "Display every N iterations (>= 1): ";
    std::cin >> display_every;
  } while (display_every < 1);

  /// Read image
  CMatrix<float> ground_truth;
  ground_truth.readFromPGM("sunset.pgm");
  disp->Display(ground_truth, "PSNR (noise-free ground truth image)");

  CMatrix<float> average(ground_truth.xSize(), 
                         ground_truth.ySize(), 
                         0.f);
  
  for (int i = 0; i < number_of_samples; ++i) {
    /// Create new noisy image
    CMatrix<float> sample(ground_truth);
    AddGaussianNoise(sample, sigma, false);
    /// PSNR of this sample
    std::cout << "PSNR of noisy sample " << i+1
              << ": " << PSNR(ground_truth, sample) << " dB\n";
    /// Average all noisy samples
    for (int y = 0; y < average.ySize(); ++y) {
      for (int x = 0; x < average.xSize(); ++x) {
        average(x,y) = (i*average(x,y) + sample(x,y)) / (i+1);
      }
    }
    /// PSNR of up-to-now average
    std::cout << "PSNR of average over " << i+1 << " noisy samples: "
              << PSNR(ground_truth, average)  << " dB\n";
    if (i%display_every == 0){
      disp->Display(Clamp(sample), "PSNR (current noisy sample)");
      disp->Display(Clamp(average), "PSNR (average over all noisy samples)");
    }

  }
  average.writeToPGM("sunsetNoisyAverage.pgm");
}


/**
 * @brief Part 3: Difference image
 */
void Ex01_c_DiffImg()
{
  std::cout << "----- Difference image -----\n";

  CTensor<float> bg;
  bg.readFromPPM("SidenbladhBG.ppm");
  CTensor<float> fg;
  fg.readFromPPM("Sidenbladh.ppm");

  CTensor<float> result(bg);
  for ( int z = 0; z < result.zSize(); ++z ) {
    for ( int y = 0; y < result.ySize(); ++y ) {
      for ( int x = 0; x < result.xSize(); ++x ) {
        result(x,y,z) = fabs(bg(x,y,z) - fg(x,y,z));
      }
    }
  }

  result.writeToPPM("Sidenbladh_diff.ppm");

  disp->Display(bg, "Difference image (first image)");
  disp->Display(fg, "Difference image (second image)");
  disp->Display(result, "Difference image (difference)");
}


/**
 * @brief Filter image in X direction
 *
 * @param result Result
 * @param image Input image 
 * @param filter1d 1d filter coefficients
 */
void FilterX(CMatrix<float>& result,
             const CMatrix<float>& image,
             const std::vector<float>& filter1d)
{
  const int filter_offset = (filter1d.size()-1)/2;

  for (int y = 0; y < image.ySize(); ++y) {
    for (int x = 0; x < image.xSize(); ++x) {
      float response = 0.f;
      for (int i = -filter_offset; i <= filter_offset; ++i) {
        int _x = x+i;
        /// Enforce Neumann boundary condition (mirror image)
        if (_x < 0) {
          _x = -1*_x;
        } else if (_x >= image.xSize()) {
          _x = 2*(image.xSize()-1)-_x;
        }
        response += image(_x, y) * filter1d[i+filter_offset];
      }
      /// Clamp result to [0,255]
      result(x,y) = std::max(0.f, std::min(response, 255.f));
    }
  }
}

/**
 * @brief Filter image in Y direction
 *
 * @param result Result
 * @param image Input image 
 * @param filter1d 1d filter coefficients
 */
void FilterY(CMatrix<float>& result,
             const CMatrix<float>& image,
             const std::vector<float>& filter1d)
{
  const int filter_offset = (filter1d.size()-1)/2;

  for (int y = 0; y < image.ySize(); ++y) {
    for (int x = 0; x < image.xSize(); ++x) {
      float response = 0.f;
      for (int i = -filter_offset; i <= filter_offset; ++i) {
        int _y = y+i;
        /// Enforce Neumann boundary condition (mirror image)
        if (_y < 0) {
          _y = -1*_y;
        } else if (_y >= image.ySize()) {
          _y = 2*(image.ySize()-1)-_y;
        }
        response += image(x, _y) * filter1d[i+filter_offset];
      }
      /// Clamp result to [0,255]
      result(x,y) = std::max(0.f, std::min(response, 255.f));
    }
  }
}



/**
 * @brief Gaussian filter
 *
 * @param image Image to filter
 * @param sigma Standard deviation parameter for normal distribution
 */
void GaussianFilter(CMatrix<float>& image,
                    float sigma)
{
  /// Create filter for a 3-sigma interval
  size_t filter_size = size_t(6*sigma+1);
  if (filter_size % 2 == 0)
    ++filter_size;
  size_t filter_offset = (filter_size-1)/2;
  std::vector<float> filter1d(filter_size);
  for (size_t i = 0; i <= filter_offset; ++i) {
    float v = (1./(std::sqrt(2*PI)*sigma)) *
              std::exp(-square((int)i)/(2*square(sigma)));
    filter1d[filter_offset-i] = v;
    filter1d[filter_offset+i] = v;
  }

  /// X direction
  CMatrix<float> resultX(image);
  FilterX(resultX, image, filter1d);
  resultX.writeToPGM("chinaToilet_Gaussian_X.pgm");
  
  /// Y direction
  CMatrix<float> resultXY(image);
  FilterY(resultXY, resultX, filter1d);

  /// Write result
  resultXY.writeToPGM("chinaToilet_Gaussian.pgm");

  disp->Display(image,    "Gaussian filter (original image)");
  disp->Display(resultX,  "Gaussian filter (only X pass)");
  disp->Display(resultXY, "Gaussian filter (result)");
}


/**
 * @brief Iterative box filter
 *
 * @param image The image to be smoothed
 * @param sigma Standard deviation for the Gaussian approximated
 *              by the box filter
 * @param iterations Number of iteration for the box filter (the
 *              higher, the better the approximation)
 */
void BoxFilter(CMatrix<float>& image,
               float sigma,
               int iterations)
{
  disp->Display(image,    "Box filter (original image)");

  /// Create box filter for [-sigma, sigma]
  size_t filter_size = size_t(2*sigma+1);
  std::vector<float> filter1d(filter_size, 1./filter_size);

  CMatrix<float> resultX(image);
  CMatrix<float> resultXY(image);

  for (int i = 0; i < iterations; ++i) {
    /// X direction
    FilterX(resultX, resultXY, filter1d);
    /// Y direction
    FilterY(resultXY, resultX, filter1d);
    disp->Display(resultXY, "Box filter (result)");
  }

  /// Write result
  resultXY.writeToPGM("chinaToilet_Box.pgm");
}


/**
 * @brief Recursive filter (This filter assumes a constant-zero 
 *        boundary condition)
 *
 * @param image The image to be smoothed
 * @param sigma Standard deviation for the Gaussian approximated
 *              by the recursive filter
 */
void RecursiveFilter(CMatrix<float>& image,
                     float sigma)
{
  disp->Display(image, "Recursive filter (original image)");

  /// Precompute some constants
  const float alpha = 5./(2.*sigma*std::sqrt(PI));
  const float ea  = std::exp(-alpha);
  const float e2a = std::exp(-2.*alpha);
  const float c0  = square(1.-ea) / (1.+2*alpha*ea-e2a);
  const float c1  = ea*(alpha-1.);
  const float c2  = ea*(alpha+1.);

  /// _____X direction_____
  {
    /// Forward pass
    CMatrix<float> f(image);
    for (int y = 0; y < image.ySize(); ++y) {
      float fi  = 0.f;  // f_i
      float fi1 = 0.f;  // f_{i-1}
      float fi2 = 0.f;  // f_{i-2}
      float Ii  = 0.f;  // I_i
      float Ii1 = 0.f;  // I_{i-1}
      for (int x = 0; x < image.xSize(); ++x) {
        Ii1 = Ii;
        Ii = image(x,y);
        fi2 = fi1;
        fi1 = fi;
        fi = c0*(Ii+c1*Ii1) + 2*ea*fi1 - e2a*fi2;
        f(x,y) = fi;
      }
    }

    /// Backward pass
    CMatrix<float> g(image);
    for (int y = 0; y < image.ySize(); ++y) {
      float gi  = 0.f;  // g_i
      float gi1 = 0.f;  // g_{i+1}
      float gi2 = 0.f;  // g_{i+2}
      float Ii  = 0.f;  // I_i
      float Ii1 = 0.f;  // I_{i+1}
      float Ii2 = 0.f;  // I_{i+2}
      for (int x = image.xSize()-1; x >= 0; --x) {
        Ii2 = Ii1;
        Ii1 = Ii;
        Ii = image(x,y);
        gi2 = gi1;
        gi1 = gi;
        gi = c0*(c2*Ii1-e2a*Ii2) + 2*ea*gi1 - e2a*gi2;
        g(x,y) = gi;
      }
    }
    
    /// Combine results
    for (int y = 0; y < image.ySize(); ++y) {
      for (int x = 0; x < image.xSize(); ++x) {
        image(x,y) = f(x,y) + g(x,y);
      }
    }
  }
  image.writeToPGM("chinaToilet_Recursive_X.pgm");
  disp->Display(image, "Recursive filter (only X pass)");

  /// _____Y direction_____
  {
    /// Forward pass
    CMatrix<float> f(image);
    for (int x = 0; x < image.xSize(); ++x) {
      float fi  = 0.f;  // f_i
      float fi1 = 0.f;  // f_{i-1}
      float fi2 = 0.f;  // f_{i-2}
      float Ii  = 0.f;  // I_i
      float Ii1 = 0.f;  // I_{i-1}
      for (int y = 0; y < image.ySize(); ++y) {
        Ii1 = Ii;
        Ii = image(x,y);
        fi2 = fi1;
        fi1 = fi;
        fi = c0*(Ii+c1*Ii1) + 2*ea*fi1 - e2a*fi2;
        f(x,y) = fi;
      }
    }

    /// Backward pass
    CMatrix<float> g(image);
    for (int x = 0; x < image.xSize(); ++x) {
      float gi  = 0.f;  // g_i
      float gi1 = 0.f;  // g_{i+1}
      float gi2 = 0.f;  // g_{i+2}
      float Ii  = 0.f;  // I_i
      float Ii1 = 0.f;  // I_{i+1}
      float Ii2 = 0.f;  // I_{i+2}
      for (int y = image.ySize()-1; y >= 0; --y) {
        Ii2 = Ii1;
        Ii1 = Ii;
        Ii = image(x,y);
        gi2 = gi1;
        gi1 = gi;
        gi = c0*(c2*Ii1-e2a*Ii2) + 2*ea*gi1 - e2a*gi2;
        g(x,y) = gi;
      }
    }
    
    /// Combine results
    for (int y = 0; y < image.ySize(); ++y) {
      for (int x = 0; x < image.xSize(); ++x) {
        image(x,y) = f(x,y) + g(x,y);
      }
    }
    
  }
  
  /// Write result
  image.writeToPGM("chinaToilet_Recursive.pgm");
  disp->Display(image, "Recursive filter (result)");
}


/**
 * @brief Smoothing filters
 */
void Ex01_d_Filters()
{
  std::cout << "----- Smoothing filters -----\n";
  int choice = -1;
  do {
    std::cout << "Choose type (1=Gaussian, 2=Iterative box, 3=Recursive): ";
    std::cin >> choice;
  } while (choice < 1 or choice > 3);
  
  switch (choice) {
    case 1: { 
      std::cout << "----- Gaussian filter -----\n";
      float sigma = -1.;
      do {
        std::cout << "Choose standard deviation sigma (in pixel): ";
        std::cin >> sigma;
      } while (sigma < 0.);
      CMatrix<float> image;
      image.readFromPGM("chinaToilet.pgm");
      GaussianFilter(image, sigma); 
      break;
    }
    case 2: { 
      std::cout << "----- Iterative box filter -----\n";
      float sigma = -1.;
      do {
        std::cout << "Choose standard deviation sigma (in pixel; >= 0): ";
        std::cin >> sigma;
      } while (sigma < 0.);
      int iterations = 0;
      do {
        std::cout << "Choose number of iterations (>= 1)";
        std::cin >> iterations;
      } while (iterations < 1);
      CMatrix<float> image;
      image.readFromPGM("chinaToilet.pgm");
      BoxFilter(image, sigma, iterations); 
      break;
    }
    case 3: { 
      std::cout << "----- Recursive filter -----\n";;
      float sigma = -1.;
      do {
        std::cout << "Choose standard deviation sigma (in pixel; >= 0): ";
        std::cin >> sigma;
      } while (sigma < 0.);
      CMatrix<float> image;
      image.readFromPGM("chinaToilet.pgm");
      RecursiveFilter(image, sigma); 
      break;
    }
    default: break;
  }
}





/**
 * MAIN
 */
int main(int argc, char** argv)
{
  (void)argc;
  (void)argv;

  /// Setup ImageDisplay instance
  disp = new ImageDisplay::ImageDisplay(false);

  /// So what should we do?
  int input;
  do {
    std::cout << "\n"
              << "Choose:\n\n"
              << "  (1): Additive Gaussian noise\n"
              << "  (2): PSNR\n"
              << "  (3): Difference image\n"
              << "  (4): Filters\n"
              << "\n"
              << "Your choice [1-4]: ";
    std::cin >> input;
  } while (input < 1 or input > 4);

  switch (input) {
    case 1: { Ex01_a_GaussianNoise();   break; }
    case 2: { Ex01_b_PSNR();            break; }
    case 3: { Ex01_c_DiffImg();         break; }
    case 4: { Ex01_d_Filters();         break; }
    default: throw std::runtime_error("Invalid choice");
  }

  /// Tidy up
  delete disp;

  /// Bye!
  return EXIT_SUCCESS;
}

