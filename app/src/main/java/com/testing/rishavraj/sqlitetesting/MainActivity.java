package com.testing.rishavraj.sqlitetesting;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;


public class MainActivity extends AppCompatActivity {

    EditText myInput;
    TextView myText;
    DBHandler dbHandler;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myInput = (EditText) findViewById(R.id.myText);
        myText = (TextView) findViewById(R.id.myData);
        dbHandler = new DBHandler(this, null, null, 1);

        //printing the existing database
        printDatabase();
    }

    //Adding a name to the database
    public void addButtonClicked(View view){
        Names name = new Names(myInput.getText().toString());
        dbHandler.addName(name);
        printDatabase();
    }

    //deleting names from the Database
    public void deleteButtonClicked(View view){
        String deleteText = myInput.getText().toString();
        dbHandler.deleteName(deleteText);
        printDatabase();
    }

    public void printDatabase(){
        String dbString = dbHandler.databaseToString();
        myText.setText(dbString);
        myInput.setText("");
    }
}
