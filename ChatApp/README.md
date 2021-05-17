# Let-s-Chat

## ChatApp [Hack-The-Cables]

The 60s  was the time when people did not have mobile phones. Letter-writing was prominent. Then gradually as years passed, the telephone was invented in 1876. At that time, every house did not had a telephone. In case if anybody wanted to talk to a member of a family living elsewhere, they had to stand in a long queue, for their turn to come so they can finally talk.

But now, is the 21st century! It's time to ditch those long cables of telephone and have a conversation with your friend, anytime you like ;)

## What it does:

Send messages from one device to another with the help of this application.

Helps people to connect from all over the world at any time.

## How to use in Local Machine:

Refer to the code in the github repository, and try it out own your local machine.
<p>Make sure you make necessary changes such as the IP address and hostname of your machine the code base.

## How it works:

### <b> Basically: </b>

This Chat App is based on the **Client Server Architechture** of the OSI Model.

* Client is the side who initiates the request.
* Server is the one who takes the request.

For E.g.: `www.google.com` <br>
The computer/mahine from which this url is fetched is the client, and the server is the one who is taking the request and sending bak details to the machine.

### **Implementation of the terminal-based app:**

We can visualize the app functioning like the data is first sent, then processed, and is assigned a port no. from the Operating System.

```
DATA --sendind (process)--> assigned with a PORT NO. from OS
``` 

A port is basically a socket.
<br>
A socket is a software/program that connects our processes to the internet.
Basically sockets connect applications to the outside world.

In order to connect our processes to the internet, we need tht IP address of the **machine on which the application is running (client)** and the port of the application.

### **Actual Process**

In order to send a message, the application on which the program is running (Client) sends the data of the running process to it's socket. The socket of the client side now connects the application to the outside world, and eventually sends the data to the person's socket to whom the message has to be sent. The reciever's socket sends the data to his application.

The reciever recieves the message.

Again, in order to reply to the sender, the reciever tries to send a message to him/her by typing a message in the application. Now, the application on the reciever side acts as client.

The same process gets repeated on the other person's side-<br>
The application on the sender's side sends the data to it's socket. The socket, which is already connected to the internet sends the data to the reciever's socket, and the reciever's socket eventually sends the data to the reciever's application and hence the message gets delivered to the reciever.

```
APPLICATION <--------[INTERNET]------------> APPLICATION
 (user-1)                                     (user-2)
```

<hr>
<br>

<p align="center">
  <img src="https://smartsensordevices.com/wp-content/uploads/2020/10/sps-datatransfer-1.gif" />
</p>
