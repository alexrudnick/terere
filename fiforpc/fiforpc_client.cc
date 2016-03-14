#include <iostream>
#include <fstream>
#include <string>

using std::string;

const string SERVER_TO_CLIENT_PATH = "/tmp/server_to_client.fifo";
const string CLIENT_TO_SERVER_PATH = "/tmp/client_to_server.fifo";

string perform_query(const string& s) {
  // Write query to server's input fifo.
  std::ofstream c2s;
  c2s.open(CLIENT_TO_SERVER_PATH.c_str());
  c2s << s;
  c2s.close();

  // Read response from server's output fifo.
  string out;
  std::ifstream s2c(SERVER_TO_CLIENT_PATH.c_str());
  std::getline(s2c, out);
  s2c.close();
  return out;
}

int main(int argc, char *argv[]) {
  string line;

  while(true) {
    bool gotline = std::getline(std::cin, line);
    if (!gotline) break;

    std::cout << "got this line: " << line << std::endl;
    string returned = perform_query(line);
    std::cout << "server returned: " << returned << std::endl;
  }
}
