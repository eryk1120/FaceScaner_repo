#include <boost/python.hpp>
#include <unistd.h>

#include <iostream>
#include <vector>
#include <string.h>     // std::string, memcpy
#include <iomanip>      // std::setw
#include <unistd.h>  //usleep
#include <sstream>  //std::ostringstream
#include <math.h>
#include "usb2lin06Controler.h"

using namespace std;
using namespace usb2lin06::controler;



int displayPatternFor(int param_a, int param_b)
{
	printf("display pattern for params: %d, %d \n", param_a, param_b);
	for(int imid = 0; imid < 15; imid++)
	{
		printf( "image %d \n", imid);
		usleep(10000);
	}
	return 0;
}


/*
*
*WARNING: dangerous
* this will move towards goal
* TODO : stop if cannot move
*/

int getStatus(){
    usb2lin06Controler controler;
    const statusReport& r = controler.report;

    controler.getStatusReport();

    return r.ref1.pos;
}

bool Up(){
    usb2lin06Controler controler;
    controler.moveUp();
}

bool Down(){
    usb2lin06Controler controler;
    controler.moveDown();
}

bool Stop(){
    usb2lin06Controler controler;
    controler.moveEnd();
}

bool moveToInternal(usb2lin06Controler & controler, uint16_t target)
{
    const statusReport& r = controler.report;

    const unsigned int max_a = 3; unsigned int a = max_a;//stuck protection
    uint16_t oldH = 0;

    const int epsilon = 13;//this seems to be move prcision

    while (true)
    {
        DEBUGOUT("%s %d", "moveTo()", target);
        controler.move(target);
        //controler.moveUp();

        usleep(200000);

        if (controler.getStatusReport())
        {
            double distance = r.ref1cnt - r.ref1.pos;
            double delta = oldH - r.ref1.pos;

            if (fabs(distance) <= epsilon | fabs(delta) <= epsilon | oldH == r.ref1.pos)
                a--;
            else
                a = max_a;

            cout
                << "current height: " << dec << setw(5) << setfill(' ') << r.ref1.pos
                << " target height: " << dec << setw(5) << setfill(' ') << target
                << " distance:" << dec << setw(5) << setfill(' ') << distance
                << endl;

            if (a == 0) { break; }
            oldH = r.ref1.pos;
        }
    }//while

    return (fabs(r.ref1.pos - target) <= epsilon);
}

void printHelp()
{
    cout << "this will set height of your desk using usb2lin06" << endl
        << "WARNING: this might be dangerous please make sure that you dont hit something!" << endl
        << "please start program with: arg1 (height)" << endl;
}

int moveTo(int targetHeight)
{
	bool succes = false;

    try {
        DEBUGOUT("main() - init");
        usb2lin06Controler controler;

        DEBUGOUT("%s %d", "main() - move to targetHeight", targetHeight);
        {
            if (moveToInternal(controler, targetHeight))
            {
                succes = true;
            }
        }

    }
    catch (usb2lin06::controler::exception e) {
        std::cerr << "Error: " << " " << e.what() << std::endl;
        return e.getErrorCode();
    }

    DEBUGOUT("main() - end");
    {
        cout << "DONE " << (succes ? "success" : "failed") << endl;
    }
    return (succes ? RETURN_CODES::OK : -1);
}

BOOST_PYTHON_MODULE(fotosfera)
{
    using namespace boost::python;
    def("displayPatternFor", displayPatternFor);
    def("moveTo", moveTo);
    def("getStatus", getStatus);
    def("Up", Up);
    def("Down", Down);
    def("Stop", Stop);
}