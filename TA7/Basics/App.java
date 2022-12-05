package Basics;

public class App {

    public static void main(String[] args)  throws InterruptedException{

        final Processor processor = new Processor();

        Thread t1 = new Thread(new Runnable() {

            @Override
            public void run() {
                try {
                    processor.produce();
                }
                catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        t1.setName("Thread 1");


        Thread t2 = new Thread(() -> {
            try {
                processor.consume();
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        t2.setName("Thread 2");

        t1.start();
        t2.start();

        t1.join();
        t2.join();
    }
}
