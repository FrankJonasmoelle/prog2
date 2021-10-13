#include <cstdlib>
// Integer class

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
		int internal_fib(int);
	private:
		int val;
	};

Integer::Integer(int n){
	val = n;
	}

int Integer::get(){
	return val;
	}

void Integer::set(int n){
	val = n;
	}


int Integer::fib(){
	int n = get();
	return internal_fib(n);
}

int Integer::internal_fib(int n){
    if (n <= 1){
		return n;
	}
	else{
		return internal_fib(n-1) + internal_fib(n-2);
	}
}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_fib(Integer* integer) {return integer->fib();}
	int Integer_internal_fib(Integer* integer, int n) {return integer->internal_fib(n)}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}