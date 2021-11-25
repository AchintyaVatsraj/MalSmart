package in.lolt3under.progressbar_sp_lab;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.os.Handler;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private ProgressBar progressBar;
    private TextView progressText;
    int i = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.setTitle("MalSmart Mobile Security");

        // set the id for the progressbar and progress text
        progressBar = findViewById(R.id.progress_bar);
        progressText = findViewById(R.id.progress_text);

        final Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                // set the limitations for the numeric
                // text under the progress bar
                if (true) {
                    progressText.setText("MalSmart");
                    progressBar.setProgress(i);
                    i++;
                    handler.postDelayed(this, 300);
                } else {
                    handler.removeCallbacks(this);
                }
            }
        }, 200);
    }
}
