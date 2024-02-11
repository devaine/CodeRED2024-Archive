using System;
using System.Collections.Generic;
using System.Text;
using System.Console;

namespace std {
    class Main {
        public void Start() {
            String prompt = "test";
            String[] options = {"ha", "test"};

            Menu mainMenu = new Menu(prompt, options);
        }
    }
}