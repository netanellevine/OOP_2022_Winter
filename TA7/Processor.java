import java.util.Scanner;

public class Processor {

    public void produce() throws InterruptedException {
        synchronized (this) {
            System.out.println(Thread.currentThread().getName() + "-> Producer thread is running....");
            wait();
            System.out.println(Thread.currentThread().getName()  + "-> Resumed...");
        }
    }


    public void consume() throws InterruptedException {

        Scanner scanner = new Scanner(System.in);
        Thread.sleep(2000);

        synchronized (this) {
            System.out.println(Thread.currentThread().getName()  + "-> Waiting for return key ->");
            scanner.nextLine();
            System.out.println(Thread.currentThread().getName()  + "-> Return key pressed...");
            notify();
//            Thread.sleep(5000);
        }
    }


}
