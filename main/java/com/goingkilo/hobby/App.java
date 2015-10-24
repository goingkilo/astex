package com.goingkilo.hobby;

import java.io.IOException;
import java.io.InputStream;

import org.python.util.PythonInterpreter;

/**
 * Hello world!
 *
 */
public class App {
	public static void main(String[] args) throws IOException {
		new App().loadRun();
	}

	public void loadRun() throws IOException {

		System.out.println("hello world");
		InputStream istr = this.getClass().getClassLoader().getResourceAsStream("com/goingkilo/hobby/main.py");
		System.out.println(istr);
		StringBuffer buf = new StringBuffer();
		byte[] b = new byte[istr.available()];
		istr.read(b);
		istr.close();
		PythonInterpreter python = new PythonInterpreter();
		python.exec(new String(b));

	}
}
