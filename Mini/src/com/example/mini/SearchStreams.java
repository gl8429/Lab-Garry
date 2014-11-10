package com.example.mini;

import android.support.v7.app.ActionBarActivity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;

public class SearchStreams extends ActionBarActivity {

	String[] streamarray;
	String[] coverurlarray;


	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_search_streams);
		Intent intent = getIntent();
		streamarray = intent.getStringArrayExtra("streamarray");
		coverurlarray = intent.getStringArrayExtra("coverurlarray");

		ArrayAdapter<String> adapter = new ArrayAdapter<String>(
				SearchStreams.this,
				R.layout.support_simple_spinner_dropdown_item, streamarray);
		
		AutoCompleteTextView auto = (AutoCompleteTextView) this
				.findViewById(R.id.autoCompleteTextView1);
		auto.setAdapter(adapter);

	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.search_streams, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}
}
