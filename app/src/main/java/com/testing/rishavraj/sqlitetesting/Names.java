package com.testing.rishavraj.sqlitetesting;

public class Names {

    private int _id;
    private String _personname;

    //initialized empty constructor for cases when we just wish to
    // create an object but set names to them later on.
    public Names(){

    }

    //initializing objects with names
    public Names(String personname) {
        this._personname = personname;
    }

    //setting values to them
    public void set_id(int _id) {
        this._id = _id;
    }

    public void set_personname(String _personname) {
        this._personname = _personname;
    }

    //getting values from the function
    public int get_id() {
        return _id;
    }

    public String get_personname() {
        return _personname;
    }

}