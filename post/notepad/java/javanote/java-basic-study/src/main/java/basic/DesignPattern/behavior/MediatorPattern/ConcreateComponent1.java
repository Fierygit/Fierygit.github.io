package basic.DesignPattern.behavior.MediatorPattern;

/**
 * @author Firefly
 * @version 1.0
 * @date 2019/11/29 15:39
 */

public class ConcreateComponent1 extends Component {

    public void dosomething(){
       mediator.dosomething(1);
    }

    public void display(){
        System.out.println("this is component1");
    }



}
