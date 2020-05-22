# fft_lu_ct
Own fft algorithm based on lookup tables and cooley tukey

# comments

- This example is an excerpt from my project for my doctoral thesis. In my thesis I measure net voltage and current consumption with analog readings.... Here you can use my fft algorithm with a simple test environment based on Python script and microcontrollers supported by Arduino IDE.
- I used Python 3.8 on Spyder IDE to create the .py files. Older versions of Python 3.x will probably work as well.
- I used Arduino IDE to create .ino and .h files, where some .h files will be written automatically out of Python script. Follow the "How to use" steps to understand how it works.
- As µC I used ESP32 because it's able to use 32Bit floating point unit (FPU) and it's pretty cheap, with connectivity to Wifi and so on.
- The highest sample rate I was able to perform was N = 128. Feel free to test any lower sample rates with N = 2^k, because the fft algorithm needs sample rates with power of 2 e.g. N = 64, N = 32, .... If you're able to run higher sample rates than N = 128, pls let me know ;-). The lookup table in Lookup.h is prepared for N <= 1024.
- You don't need to change N in the arduino project! It'll be calculated out of Signal.h You must change N only in fourier_setup.py
- The time expenditure for fft algorithm depends on the sample rate N and the accuracy in the for-loop of the rootdiv() in Func.h.
  In fft() you can choose between rootdiv(),based on heron algorithm, and sqrt() standard function.
- The harmonics become mirrored around the half of sample rate times fundamental frequency with respect to Nyquist–Shannon sampling theorem

# How to use?

Step 1: Start "fourier_setup.py", create your testsignal "y". "n" must be an integer multiple of the sample rate "N" e.g. n = 1024, N = 128. 

Step 2: You can choose between 
  - fft_c (FFT based on cartesian coordinates), --> implemented in Arduino project as well
  - fft_p (FFT based on polar coordinates),
  - dft_c (DFT based on cartesian coordinates),
  - dft_p (DFT based on polar coordinates),
  to compare how the different methods perform.
 
Step 3: A testsignal will be create automatically in "Signal.h", which is part of the Arduino project.

Step 4: Start the Arduino IDE with "FFT_Test.ino". Restart Arduino IDE everty time after you changed "Signal.h" to take effect!

Step 5: Choose Controller Board and flash the project. In my case ESP32 Dev Module.

Step 6: Open Serial Monitor. The harmonics of the test signal "x" from "Signal.h" will be shown.
