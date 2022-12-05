package Deadlock;

public class TestDeadlockExample1 {
    public static void main(String[] args) {
        final String resource1 = "My resource";
        final String resource2 = "My better resource";
        // t1 tries to lock resource1 then resource2

        Thread t1 = new Thread() {
            public void run() {
                synchronized (resource1) {
                    System.out.println("Thread 1: locked resource 1");

                    try { Thread.sleep(100);} catch (Exception e) {}

                    synchronized (resource2) {
                        System.out.println("Thread 1: locked resource 2");
                    }
                }
            }
        };

        // t2 tries to lock resource2 then resource1
        Thread t2 = new Thread() {
            public void run() {
                synchronized (resource2) {
                    System.out.println("Thread 2: locked resource 2");

                    try { Thread.sleep(100);} catch (Exception e) {}

                    synchronized (resource1) {
                        System.out.println("Thread 2: locked resource 1");
                    }
                }
            }
        };


        t1.start();
        t2.start();
    }
}

/**
 * How to avoid deadlock?
 * A solution for a problem is found at its roots.
 * In deadlock, it is the pattern of accessing the
 * resources A and B, is the main issue. To solve the
 * issue we will have to simply re-order the statements
 * where the code is accessing shared resources.
 *
 * Another example:
 * Thread 1 locks A, waits for B
 *
 * Thread 2 locks B, waits for C
 *
 * Thread 3 locks C, waits for D
 *
 * Thread 4 locks D, waits for A
 *
 * Thread 1 waits for thread 2, thread 2 waits for thread 3, thread 3 waits for thread 4, and thread 4 waits for thread 1.
 */