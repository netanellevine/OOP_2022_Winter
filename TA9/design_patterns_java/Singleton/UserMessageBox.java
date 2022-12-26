package design_patterns_java.Singleton;

public class UserMessageBox {
    private static SystemMessageBox messageBox=null;

    public static SystemMessageBox getMessageBox(){
        if(messageBox==null){
            messageBox=new SystemMessageBox();
        }
        return messageBox;
    }

    public static void addUser(int userID){
        messageBox.addUser(userID);
    }

    public static void sendMessage(int toUserID, Message message){
        messageBox.sendMessage(toUserID, message);
    }

    public static boolean isEmpty(int userID){
        return messageBox.isEmpty(userID);
    }

    public Message read(int userID) {
        return messageBox.read(userID);
    }
}
