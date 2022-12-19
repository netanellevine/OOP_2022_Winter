package Lesson8.Adapter;

public class OrderButton implements Drunkable{
    private BeerBottle bottle;

    @Override
    public void orderBeer() {
        bottle.getBeerFromBottle();
    }
}
