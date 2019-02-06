# Video stream from raspberry pi

The raspberry pi is an amazing onboard computer, but it lacks the computing power to do much powerful stuff like image processing. The scripts allow you to stream the raw video from the raspberry pi to your computer which has more processing power. Even the compression part is done on the client computer. The stream received on the other end is OpenCV compatible and offers a delay of less than 150ms.

## Getting Started

Download the server script to rpi. Download the client and test scripts to your computer.

### Prerequisites

You need to have ffmpeg installed on the client computer.

```
sudo apt install ffmpeg
```

### Setup

Both the rpi and the client computer need to be on the same network.

Find out the ip address of the client computer.

For Ubuntu 18

```
ip a
```

For Ubuntu 16

```
ifconfig
```

The ip address will be of the form 192.168.0.10

Modify the server script on the rpi. Change the ip address to that of the client

```
nano server.sh
```

## Running the stream

### client

Run the client script followed by the test script

```
./client.sh
```

In a new terminal

```
python test.py
```

### server

After setting up the client, run the server script on rpi

```
server.sh
```
