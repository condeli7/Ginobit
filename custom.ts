
/**
* Use this file to define custom functions and blocks.
* Read more at https://makecode.microbit.org/blocks/custom
*/

enum MyEnum {
    //% block="one"
    One,
    //% block="two"
    Two
}

/**
 * Custom blocks
 */
//% weight=100 color=#0fbc11 icon=""
namespace ginobit {
    /**
      * TODO: Commands the Ginobot to move forward with speed x (0-100)
      * @param speed speed value (0-100), eg: 100
      */
    //% block="move forward $speed"
    export function move_forward(speed: number): void {
        // Add code here
    }

    /**
      * TODO: Commands the Ginobot to move backwards with speed x (0-100)
      * @param speed speed value (0-100), eg: 100
      */
    //% block="move backwards $speed"
    export function move_backwards(speed: number): void {
        // Add code here
    }

    /**
     * TODO: describe your function here
     * @param value describe value here, eg: 5
     */
    //% block
    export function fib(value: number): number {
        return value <= 1 ? value : fib(value -1) + fib(value - 2);
    }
}
