using UnityEngine;                                              // 'using' directives are above the class declaration, with space before the class
using System.Collections;

public class StyleGuide_SASCS : MonoBehaviour                   // class declaration is left-justified (no spaces before it)
{                                                               /* opening { for classes, for loops, functions, conditionals, etc. are 
                                                                aligned with the declaration */   
    // declare (and initialize) all global variables                                
    float x_Start;                                              // all enclosed code is indented by one tabspace
    float y_Start;                                              /* all action lines [declaring/setting a variable, 
                                                                   calling a function, etc.]) end with semicolon */

    float grid_Width = 10;                                      // Whether you choose camelCase, PascalCase, or under_Scores, keep it consistent
    float grid_Height = 20;
    GameObject[ , ] grid;

    float time_Elapsed;

    // Start is called before the first frame update
    void Start()                                                
    {                                                           // again, { is aligned with the function declaration
        x_Start = - gridWidth * xSpace / 2;                     // again, all code within a pair of {} is indented one tabspace from its parent
        y_Start = gridHeight * ySpace / 2;
        grid = new GameObject[gridWidth, gridHeight];           // related lines of code are vertically dense
                                                                // separate ideas have 1 or 2 lines of space between
                                                                
        // check all numbers 0 thru 99 for even/odd             //comments to explain a block of code should be right before
        
        for (int i = 0; i < 100; i++)
        {
            if ((i % 2) == 0) // use modulo to check each #     // comments to explain one line can be inline
            {                                                   // conditionals/for loops can have opening curly braces inline
                Debug.Log("even!");
            }
            else
            {
                Debug.Log("odd!");
            }                                                   // } should still be aligned with the thing it's storing
        }

    }
}
