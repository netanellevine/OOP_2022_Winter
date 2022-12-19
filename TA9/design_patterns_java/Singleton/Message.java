package design_patterns_java.Singleton;

public class Message {
    private final int fromUserID;
    private final String content;

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
