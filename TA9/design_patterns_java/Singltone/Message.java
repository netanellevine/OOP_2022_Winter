package Lesson8.Singltone;

public class Message {
    private int fromUserID;
    private String content;

    public Message(int fromUserID, String content) {
        this.fromUserID = fromUserID;
        this.content = content;
    }

    public int getFromUserID() {
        return fromUserID;
    }

    public String getContent() {
        return content;
    }
}
