package Lesson8.Singltone;

import java.util.ArrayList;

public class MessageBox {
    private ArrayList<Message> incoming;
    public MessageBox(){
        incoming=new ArrayList<>();
    }

    public synchronized boolean isEmpty(){
        return this.incoming.size() == 0;
    }

    public synchronized Message readMessage(){
        if(isEmpty()){
            return new Message(-1, "No new messages");
        }
        return this.incoming.remove(0);
    }

    public synchronized void sendMessage(Message message){
        this.incoming.add(message);
    }
}
