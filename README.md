# 개발 환경
  Hard ware <br>
  1. Raspberry Pi 3 Model B<br>
  2. USB Web cam<br>
  3. Desktop PC<br>
  <br>Soft ware <br>
  1. OpenCV 3.4.1<br>
  2. PyQt5<br>
  3. Putty<br>
  4. WinSCP<br>
  5. Python3<br>

# 개발환경 셋팅
  1. 라즈비안 설치<br>
    https://www.raspberrypi.org/downloads/raspbian/ 홈페이지 들어가 라즈비안 이미지 파일 다운로드
    micro sd카드 포멧후 이미지 파일 씌우기 (window 에서 이미지 파일 씌우는 프로그램 http://sourceforge.net/projects/win32diskimager/
    
  2. 5 inch LCD setting<br>
    boot 폴더에 config.txt 맨하단에 
    hdmi_group=2
    hdmi_mode=87
    hdmi_cvt=800 480 60 6
    hdmi_drive=1
    을 입력한다
    터치를 하려면 http://www.waveshare.com/wiki/5inch_HDMI_LCD 홈페이지에서 LCD-show-160811.tar.gz 설치후 boot 폴더에 넣은 다음
    명령어 라인에 
    tar xzvf /boot/LCD-show-160811.tar.gz  
    cd LCD-show/
    /LCD5-show
    실행을 하고 reboot하면 된다
    
  3. opencv 3.4.1 설치<br>
      - putty로 라즈비안에 접속을 하여 opencv 2.4버전 제거 
        명령어 라인에
        sudo apt-get purge  libopencv* python-opencv
        sudo apt-get autoremove
        
      - 기존 패키지 업그레이드
        명령어 라인에
        sudo apt-get update
        sudo apt-get upgrade
        
      - OpenCV 컴파일 전에 필요한 패키지 설치
        명령어 라인에
        sudo apt-get install build-essential cmake
        sudo apt-get install pkg-config
        sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
        sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
        sudo apt-get install libv4l-dev v4l-utils
        sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 
        sudo apt-get install libgtk2.0-dev
        sudo apt-get install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev   
        sudo apt-get install libatlas-base-dev gfortran libeigen3-dev
        sudo apt-get install python2.7-dev python3-dev python-numpy python3-numpy
        
      - OpenCV 설정과 컴파일 및 설치
        명령어 라인에
        mkdir opencv
        cd opencv
        wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.1.zip
        unzip opencv.zip
        wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip
        unzip opencv_contrib.zip
        cd opencv-3.4.1
        mkdir build
        cd build
        cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D WITH_TBB=OFF \
        -D WITH_IPP=OFF \
        -D WITH_1394=OFF \
        -D BUILD_WITH_DEBUG_INFO=OFF \
        -D BUILD_DOCS=OFF \
        -D INSTALL_C_EXAMPLES=ON \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D BUILD_EXAMPLES=OFF \
        -D BUILD_TESTS=OFF \
        -D BUILD_PERF_TESTS=OFF \
        -D ENABLE_NEON=ON \
        -D ENABLE_VFPV3=ON \
        -D WITH_QT=OFF \
        -D WITH_GTK=ON \
        -D WITH_OPENGL=ON \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.4.1/modules \
        -D WITH_V4L=ON \
        -D WITH_FFMPEG=ON \
        -D WITH_XINE=ON \
        -D BUILD_NEW_PYTHON_SUPPORT=ON \
        ../
        make -j4
        sudo make install
        
      - python 으로 opencv 설치 확인
        python
        import cv2
        
  4. PyQt5 설치<br>
    명령어 라인에 
    sudo apt-get update
    sudo apt-get upgrade 
    sudo apt-get install python3-pyqt5

# 제작의도
  크기가 크고 가격이 비싼 Gel Doc을 가격이 저렴하고 쉽게 구할 수 있는 RaspberryPi와 Webcam으로 대체 하기 위해

# 용도
  DNA나 RNA, protein 와 같은 큰 분자 들을 전기적인 힘으로 gel에서 이동한 형광 물질을 이용하여 이미지 화 하기 위해서

# UI
  (노출값과 focus값을 제어하고 캡처기능을 함)
  
#
#
#
#
