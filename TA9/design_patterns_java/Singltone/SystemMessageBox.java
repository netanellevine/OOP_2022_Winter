package Lesson8.Singltone;


import java.util.HashMap;

public class SystemMessageBox {

    private HashMap<Integer, MessageBox> systemBox;

    public SystemMessageBox(){
        this.systemBox=new HashMap<>();
    }

    public synchronized void addUser(int userID){
        if(this.systemBox.containsKey(userID)){
            return;
        }
        this.systemBox.put(userID, new MessageBox());
    }

    public void sendMessage(int toUserID, Message message){
        if(this.systemBox.containsKey(toUserID) && message!=null){
            this.systemBox.get(toUserID).sendMessage(message);
        }
        return;
    }

    public boolean isEmpty(int userID){
        if(this.systemBox.containsKey(userID)){
            return this.systemBox.get(userID).isEmpty();
        }
        return false;
    }

    public Message read(int userID){
        if(this.systemBox.containsKey(userID)){
            return this.systemBox.get(userID).readMessage();
        }
        return new Message(-1, "No message available");
    }
}
