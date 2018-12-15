# 개발 환경
  
    Hard ware 
      1. Raspberry Pi 3 Model B
      2. USB Web cam
    
    Soft ware 
      1. OpenCV 3.4.1
      2. PyQt5
      3. Putty
      4. WinSCP
      5. Python3

# 개발환경 셋팅
  1. 라즈비안 설치<br>
    https://www.raspberrypi.org/downloads/raspbian/ 홈페이지 들어가 라즈비안 이미지 파일 다운로드
    micro sd카드 포멧후 이미지 파일 씌우기 (window 에서 이미지 파일 씌우는 프로그램 http://sourceforge.net/projects/win32diskimager/
    
  2. 5 inch LCD setting<br>
    boot 폴더에 config.txt 맨하단에 <br>
    hdmi_group=2<br>
    hdmi_mode=87<br>
    hdmi_cvt=800 480 60 6<br>
    hdmi_drive=1<br>
    을 입력한다
    터치를 하려면 http://www.waveshare.com/wiki/5inch_HDMI_LCD 홈페이지에서 LCD-show-160811.tar.gz 설치후 boot 폴더에 넣은 다음
    명령어 라인에 
    tar xzvf /boot/LCD-show-160811.tar.gz  <br>
    cd LCD-show/<br>
    /LCD5-show<br>
    실행을 하고 reboot하면 된다
    
  3. opencv 3.4.1 설치<br>
      - putty로 라즈비안에 접속을 하여 opencv 2.4버전 제거 
        명령어 라인에
        sudo apt-get purge  libopencv* python-opencv<br>
        sudo apt-get autoremove<br>
        
      - 기존 패키지 업그레이드
        명령어 라인에
        sudo apt-get update<br>
        sudo apt-get upgrade<br>
        
      - OpenCV 컴파일 전에 필요한 패키지 설치
        명령어 라인에<br>
        sudo apt-get install build-essential cmake (build-essential 패키지에는 C/C++ 컴파일러와 관련 라이브러리, make 같은 도구들이 포함되어 있습니다. cmake는 컴파일 옵션이나 빌드된 라이브러리에 포함시킬 OpenCV 모듈 설정등을 위해 필요합니다.)<br><br>
        sudo apt-get install pkg-config (pkg-config는 프로그램 컴파일 및 링크시 필요한 라이브러리에 대한 정보를 메타파일(확장자가 .pc 인 파일)로부터 가져오는데 사용됩니다. 터미널에서 특정 라이브러리를 사용한 소스코드를 컴파일시 필요한 컴파일러 및 링커 플래그를 추가하는데 도움이 됩니다.)<br><br>
        sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev (특정 포맷의 이미지 파일을 불러오거나 기록하기 위해 필요한 패키지들입니다.)<br><br>
        sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev (특정 코덱의 비디오 파일을 읽어오거나 기록하기 위해 필요한 패키지들입니다.)<br><br>
        sudo apt-get install libv4l-dev v4l-utils (Video4Linux 패키지는 리눅스에서 실시간 비디오 캡처를 지원하기 위한 디바이스 드라이버와 API를 포함하고 있습니다.)<br><br>
        sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev (GStreamer는 비디오 스트리밍을 위한 라이브러리입니다.)<br><br>
        sudo apt-get install libgtk2.0-dev (OpenCV에서는 highgui 모듈을 사용하여 자체적으로 윈도우 생성하여 이미지나 비디오들을 보여줄 수 있습니다. 윈도우 생성 등의 GUI를 위해 gtk 또는 qt를 선택해서 사용가능합니다.  여기서는 gtk2를 지정해주었습니다.)<br><br>
        sudo apt-get install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev (OpenGL 지원하기 위해 필요한 라이브러리입니다.)<br>  <br>
        sudo apt-get install libatlas-base-dev gfortran libeigen3-dev (OpenCV 최적화를 위해 사용되는 라이브러리들입니다.)<br><br>
        sudo apt-get install python2.7-dev python3-dev python-numpy python3-numpy (python2.7-dev와 python3-dev 패키지는 OpenCV-Python 바인딩을 위해 필요한 패키지들입니다. Numpy는 매트릭스 연산등을 빠르게 처리할 수 있어서 OpenCV에서 사용됩니다.)<br><br>
        
      - OpenCV 설정과 컴파일 및 설치
        명령어 라인에
        mkdir opencv (opencv 디렉토리 생성)<br><br>
        cd opencv (opencv 디렉토리 이동)<br><br>
        wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.1.zip (opencv 3.4.1 버전 zip 다운로드)<br><br>
        unzip opencv.zip (다운로드한 zip 파일 압축 해제)<br><br>
        wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip (opencv_contrib 3.4.1 버전 zip 다운로드)<br><br>
        unzip opencv_contrib.zip (다운로드한 zip 파일 압축 해제)<br><br>
        cd opencv-3.4.1 (opencv-3.4.1 디렉토리로 이동)<br><br>
        mkdir build (bulid 디렉토리 생성)<br><br>
        cd build (build 디렉토리로 이동 )<br><br>
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
        ../ (opencv 컴파일 설정)<br><br>
        make -j4 (make 명령어를 사용하여 컴파일)<br><br>
        sudo make install (컴파일 결과를 설치)<br><br>
        
      - python 으로 opencv 설치 확인
        python<br>
        import cv2<br>
        
  4. PyQt5 설치<br>
    명령어 라인에 
    sudo apt-get update<br>
    sudo apt-get upgrade <br>
    sudo apt-get install python3-pyqt5<br>

# 제작의도
  크기가 크고 가격이 비싼 Gel Doc을 가격이 저렴하고 쉽게 구할 수 있는 RaspberryPi와 Webcam으로 대체 하기 위해

# 용도
  DNA나 RNA, protein 와 같은 큰 분자 들을 전기적인 힘으로 gel에서 이동한 형광 물질을 이용하여 이미지 화 하기 위해서

# UI
  (노출값과 focus값을 제어하고 캡처기능을 함)<br>
  ![image](https://user-images.githubusercontent.com/38156821/43898800-ed6597ba-9c1a-11e8-9d11-513be9d4fcc4.png)

# Samba 사용하는 의도
  Samba를 이용하여 pc와 RaspberryPi간에 공유 폴더를 마운트 하여 RaspberryPi USB Webcam으로 촬영된 이미지를 pc로 자동으로 전송하기 

# Samba Window Setting
  1. 윈도우 + r 키를 누른후 control /name Microsoft.NetworkAndSharingCenter 입력<br>
  2. 고급설정 변경<br>
  3. 네트워크 검색 켜기와 파일 및 프린트 공유 켜기 체크 후 변경 내용 저장<br>
  4. 공유할 폴더를 선택하고 마우스 우클릭 후, 메뉴에서 속성을 선택합니다.<br>
     공유 탭을 선택하고 고급 공유를 클릭합니다<br>
  5. 선택한 폴더 공유를 체크하고 권한을 클릭합니다.<br>
  6. 추가를 클릭합니다.<br>
  7. 선택할 개체 이름에 라즈베리파이에서 공유폴더에 접근시 사용할 윈도우에 등록된 사용자 이름을 적어주고 확인을 클릭합니다<br>
  8. 방금 추가된 사용자를 선택하고 모든 권한의 허용을 체크해줍니다. <br>
  9. 추가한 사용자외에 다른 사람들은 공유폴더에 접근할 수 없도록 Everyone을 선택하고 제거를 클릭합니다.<br>
  10. 파일 공유시 방어벽이 문제가 안되도록 설정을 변경해줘야 합니다.<br>
      제어판에서 시스템 및 보안 > Windows 방어벽에서 앱 허용을 선택합니다.<br>
  11. 설정 변경을 클릭합니다. <br>
  12. 목록에서 파일 및 프린터 공유를 찾아서 개인 항목을 체크하고 확인을 클릭합니다.<br>
  
# Samba RaspberryPi Setting
  1. sudo apt-get install samba samba-common 명령어 실행 <br>
  2. sudo nano /etc/samba/smb.conf 명령어 실행 <br>
      global 부분에 wins support = yes 추가 
      하단에 
      [pi]
      path="경로지정"
      browseable=Yes
      writeable=Yes
      only guest=no
      guest ok = no
      create mask=0777
      directory mask=0777
      public=no<br>
  3. sudo /etc/init.d/samba restart 명령어 실행 (재실행)<br>
  4. sudo smbpasswd -a pi 명령어 실행 (패스워드 설정)<br>
  
# Window 에서 Raspberry 접근
  1. Raspberry Pi 에서 ifconfig로 ip주소확인<br>
  2. 윈도우 + R <br>
  3. \\Raspberry Pi ip주소 입력<br>
  
# Raspberry 에서 Window 접근
  1. sudo apt-get install smbclient 명령어 실행 <br>
  2. sudo smbclient -L PC IP 주소 -U PC Name 명령어 실행 으로 확안<br>
  3. sudo apt-get install cifs-utils 명령어 실행 <br>
  4. sudo mount -t cifs -o user=PC Name,file_mode=0777,dir_mode=0777 //PC IP 주소/공유폴더 /media/windows 명령어 실행 <br>
  - 마운트 해제 udo umount /media/windows<br>  

# Samba의 보완점
  같은 공유기로 접속을 한 경우(Gate way가 같은 경우)에만 폴더를 공유 할수 있다.
  그럼으로 공유기 설정으로 ip 포워드 해줌으로서 다른 Gate way이라도 파일을 공유할수 있게 한다

# Error Note
  (PyQt로 opencv를 보여줄때 발생할 수 있다.)vidioc_s_ctrl input/output error 이러한 이러한 애러가 발생시엔 focus를 auto를 해제 한다.
  (v4l2-ctl -d /dev/video0 -c focus_auto=0 명령어 실행)
  
  VIDEOIO ERROR: V4L2: Pixel format of incoming image is unsupported by OpenCV Unable to stop the stream: Device or resource busy 이러한 에러 메시지가 나오면 cam이 접촉불량이다

