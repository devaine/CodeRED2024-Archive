using System;
using System.Collection.Generic;
using System.Text;
using static System.Console;

namespace Main {
    class Menu
    {
        private int SelectedIndex;
        private String[] Options;
        private String Prompt;

        public Menu(String prompt, String[] options)
        {
            this.Prompt = prompt;
            this.Options = options;
            this.SelectedIndex = 0;
        }

        public void OptionDisplay()
        {
            WriteLine(Prompt);
            for(int i = 0; i < Options.Length; i++){
                String currentOption = Options[i];
                WriteLine($"<< {currentOption} >>");
            }
        }

        
    }
        
    
}