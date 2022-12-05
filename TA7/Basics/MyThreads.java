package Basics;

public class MyThreads {
    /**
     * New
     * Active -> Runnable(queue) and Running
     * Blocked / Waiting
     * Timed Waiting
     * Terminated
     *
     * Thread scheduler -> Priority and the Time of arrival
     * 1 - First Come, First Served Scheduling
     * 2 - Time-slicing scheduling
     * 3 - Preemptive-Priority Scheduling
     */
    public static void main(String[] args) throws InterruptedException {
         FirstMultithreading myThread = new FirstMultithreading(1);
         FirstMultithreading myThread2 = new FirstMultithreading(2);

//         myThread.setPriority(Thread.MIN_PRIORITY);
//         myThread.setPriority(Thread.NORM_PRIORITY);
//         myThread.setPriority(Thread.MAX_PRIORITY);


//        myThread.setDaemon(true);
        
//         myThread.run();
//         myThread2.run();

//        myThread.start();
//        myThread.join();
//
//        myThread2.start();
//        myThread2.join();

        // What is the difference between run and start???

//         for (int i = 0; i < 3; i++) {
//             FirstMultithreading currThread = new FirstMultithreading(i);
//             currThread.start();
//         }

//         throw new RuntimeException();


//         for (int i = 0; i < 3; i++) {
//             Basics.SecondMultithreading currThread = new Basics.SecondMultithreading(i);
//             Thread secondOption = new Thread(currThread);
//             secondOption.start();
//         }

        // why? if you want to extend any other class use the implements way...


//         for (int i = 0; i < 3; i++) {
//             FirstMultithreading currThread = new FirstMultithreading(i);
//             currThread.start();
//
//             try {
//                 currThread.join();
//             } catch (InterruptedException e) {
//                 e.printStackTrace();
//             }
//         }


//        for (int i = 0; i < 3; i++) {
//            FirstMultithreading currThread = new FirstMultithreading(i);
//            currThread.start();
//
//            System.out.println("The " + i + "'th thread is alive? " + currThread.isAlive());
//        }

    }
}
