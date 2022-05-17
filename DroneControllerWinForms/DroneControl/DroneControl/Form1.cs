using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;

namespace DroneControl
{
    public partial class Form1 : Form
    {
        SerialPort Arduino = new SerialPort("COM7", 9600);

        public Form1()
        {
            InitializeComponent();
            Arduino.Open();
        }


        private void btnForward_MouseHover(object sender, EventArgs e)
        {
            Arduino.Write("w");
        }

        private void Form1_MouseHover(object sender, EventArgs e)
        {
            Arduino.Write("r");
        }

        private void btnLeft_MouseHover(object sender, EventArgs e)
        {
            Arduino.Write("a");
        }

        private void btnRight_MouseHover(object sender, EventArgs e)
        {
            Arduino.Write("d");
        }

        private void btnBack_MouseHover(object sender, EventArgs e)
        {
            Arduino.Write("s");
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Arduino.Close();
        }
    }
}
