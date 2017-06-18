package com.testing.rishavraj.sqlitetesting;

import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.database.Cursor;
import android.content.Context;
import android.content.ContentValues;


// class is responsible for anything and everything related to database

public class DBHandler extends SQLiteOpenHelper{


    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "database.db";
    private static final String TABLE_NAMES = "names";
    private static final String COLUMN_ID = "_id";
    private static final String COLUMN_PERSONNAME = "personname";

    public DBHandler(Context context, String name, SQLiteDatabase.CursorFactory factory, int version) {
        super(context, DATABASE_NAME, factory, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String query = "CREATE TABLE " + TABLE_NAMES + "(" +
                COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COLUMN_PERSONNAME + " TEXT " +
                ");";
        db.execSQL(query);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAMES);
        onCreate(db);
    }

    //adding a new row to the database
    public void addName(Names name){
        ContentValues values = new ContentValues();
        values.put(COLUMN_PERSONNAME, name.get_personname());
        SQLiteDatabase db = getWritableDatabase();
        db.insert(TABLE_NAMES, null, values);
        db.close();
    }


    //deleting a product from the database
     public void deleteName(String personname){
         SQLiteDatabase db = getWritableDatabase();
         db.execSQL("DELETE FROM " + TABLE_NAMES + " WHERE " + COLUMN_PERSONNAME + "=\"" + personname + "\";");
     }

    //printing out the database as a string
    public String databaseToString(){
        String dbString = "";
        SQLiteDatabase db = getWritableDatabase();
        String query = "SELECT * FROM " + TABLE_NAMES + " WHERE 1";

        //cursor point out to a location in our results
        Cursor c = db.rawQuery(query, null);

        //moving it to the first row in our result
        c.moveToFirst();

        //adding data to the dbString until cursor points after the last element
        while(!c.isAfterLast()){
            if(c.getString(c.getColumnIndex("personname")) != null){
                dbString += c.getString(c.getColumnIndex("personname"));
                dbString += "\n";
            }
            c.moveToNext();
        }
        c.close();
        db.close();
        return dbString;
    }




}
