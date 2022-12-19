package Lesson8.Adapter;

/**
 * Most of the bars offer beer to their customers.
 * Beer is awesome.
 * But some bars like this one sell beer from bottle and don't tell the customer it's not from a tap.
 * Let's bring this problem into our code space and solve it.
 * let's model our objects:
 * Customer: a customer. we will want a name and an order button.
 * BeerBottle: a beer bottle.
 * Drunkable: an interface that the OrderButton object implements and used to order beer.
 * when the customer will click on the OrderButton, he will expect to get beer from the tap,
 * but instead he will get beer from a bottle
 */

public class Customer{
    private String name;
    private OrderButton button;

    public Customer(String name) {
        this.name = name;
        this.button=new OrderButton();
    }

}
