package Lesson8.Singltone;

/**
 * Assuming we want to create a safe thread message system, like chat without a server.
 * We would like to share the chat among all of the users, so we can create a common message box -
 * a singltone that all of the user have to share.
 * The singltone will contain a map of messageboxes, each belong to a different user and each messagebox
 * methods are thread safe, so 2 people can read messages at the same time from different message boxes.
 *
 * We will create the next classes:
 * Message: a message
 * MessageBox: contain a list of messages and its methods are thread safe
 * SystemMessageBox: contain map of messageboxes, each belong to a different client
 * UserMessageBox: a singltone that contains a SystemMessageBox.
 */

public class Client {
    private static int userCounter = 0;
    private int ID;
    private String UserName;
    SystemMessageBox messageBox;
    public Client(String username){
        this.UserName=username;
        this.messageBox=UserMessageBox.getMessageBox();
        synchronized (this){
            this.ID = Client.userCounter;
            Client.userCounter++;
            this.messageBox.addUser(this.ID);
        }
    }

    public void sendMessage(int toUserID, Message message){
        messageBox.sendMessage(toUserID, message);
    }

    public boolean isEmpty(int userID){
        return messageBox.isEmpty(userID);
    }

    public Message read(int userID) {
        return messageBox.read(userID);
    }
}
