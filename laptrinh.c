#include <stdio.h>

struct calculateFractions{
    float numerator;
    float denominator;
};
typedef struct calculateFractions Fraction;

float sum(Fraction fr1,  Fraction fr2){
    float calculatesum;
    calculatesum = ((fr1.numerator*fr2.denominator+fr1.denominator*fr2.numerator))/(fr1.numerator*fr2.denominator);
    return calculatesum;
}   
float difference(Fraction fr1,  Fraction fr2){
    float calculateDifference;
    calculateDifference = ((fr1.numerator*fr2.denominator+fr1.denominator*fr2.numerator))/(fr1.numerator*fr2.denominator);
    return calculateDifference;
}
float product(Fraction fr1, Fraction fr2){
    float calculateProduct;
    calculateProduct = ((fr1.numerator*fr2.numerator))/(fr1.denominator*fr2.denominator);
    return calculateProduct;
}
float quotient(Fraction fr1, Fraction fr2){
    float calculateQuotient;
    calculateQuotient = (fr1.numerator*fr2.denominator)/(fr1.denominator*fr2.numerator);
    return calculateQuotient;
}
void main(){
    Fraction frtemp1, frtemp2;
    printf("Enter the fraction nemurator 1: ");
    scanf("%f", &frtemp1.numerator);
    printf("Enter the fraction nemurator 2: ");
    scanf("%f", &frtemp2.numerator);
    
    printf("Enter the fraction denominator 1: ");
    scanf("%f", &frtemp1.denominator);
    printf("Enter the fraction denominator 2: ");
    scanf("%f", &frtemp2.denominator);

    printf("sum height of operator is: %f\n", sum(frtemp1 ,frtemp2));
    printf("difference height of operator is: %f\n", difference(frtemp1 ,frtemp2));
    printf("product height of operator is: %f\n", product(frtemp1 ,frtemp2));
    printf("quotient height of operator is: %f\n", quotient(frtemp1 ,frtemp2));
    


}
