public class MyThreads {
    public static void main(String[] args) {
        // FirstMultythread myThread = new FirstMultythread(1);
        // FirstMultythread myThread2 = new FirstMultythread(2);
        
        // myThread.run();
        // myThread2.run();

        // myThread.start();
        // myThread2.start();

        // for (int i = 0; i < 3; i++) {
        //     FirstMultythread currThread = new FirstMultythread(i);
        //     currThread.start();
        // }
        // throw new RuntimeException();


        // for (int i = 0; i < 3; i++) {
        //     SecondMultythread currThread = new SecondMultythread(i);
        //     Thread secondOption = new Thread(currThread);
        //     secondOption.start();
        // }

        // why? if you want to extend any other class use the implements way...


        // for (int i = 0; i < 3; i++) {
        //     FirstMultythread currThread = new FirstMultythread(i);
        //     currThread.start();

        //     try {
        //         currThread.join();
        //     } catch (InterruptedException e) {
        //         e.printStackTrace();
        //     }
        // }






        for (int i = 0; i < 3; i++) {
            FirstMultythread currThread = new FirstMultythread(i);
            currThread.start();

            System.out.println("The " + i + "'th thread is alive? " + currThread.isAlive());
        }

    }
}
