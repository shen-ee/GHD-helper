## darknet-tutorial-MacOS

#### Single image prediction

1. download repo: https://github.com/AlexeyAB/darknet

2. open the main folder in terminal and then make, for example:

   ```bash
   cd /change-this-to-your-path/darknet-master
   make
   ```

3. download trained model in google drive, for example: https://drive.google.com/open?id=1IFR_Bv1YZkAM8JskOK3I1P3KXi1Hnob8

4. move the .weights file into folder darknet-master, for example:

5. ```bash
   mv yolov3-ghd_final.weights /change-this-to-your-path/darknet-master/
   ```

6. download repo: https://github.com/shenyi1028/GHD-helper

7. open the main folder in terminal, copy the files into the folder in step 2, for example:

   ```bash
   cd /change-this-to-your-path/GHD-helper-master
   cp -r darknet/* /change-this-to-your-path/darknet-master
   ```

8. come back to the folder in step2, try to do a prediction:

   ```bash
   cd /change-this-to-your-path/darknet-master
   ./darknet detector test cfg/ghd.data cfg/yolov3-ghd.cfg yolov3-ghd_final.weights data/test.jpg
   ```

9. then a file named predictions.png should be genrated.

