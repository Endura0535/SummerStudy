namespace project
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.label1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.map3 = new System.Windows.Forms.PictureBox();
            this.character = new System.Windows.Forms.PictureBox();
            this.ball = new System.Windows.Forms.PictureBox();
            this.map2 = new System.Windows.Forms.PictureBox();
            this.map = new System.Windows.Forms.PictureBox();
            this.label4 = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.map3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.character)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ball)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.map2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.map)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Gulim", 40F);
            this.label1.Location = new System.Drawing.Point(483, 230);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 67);
            this.label1.TabIndex = 6;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(64, 60);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(45, 15);
            this.label3.TabIndex = 9;
            this.label3.Text = "label3";
            // 
            // map3
            // 
            this.map3.Image = global::project.Properties.Resources.map31;
            this.map3.Location = new System.Drawing.Point(330, 31);
            this.map3.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.map3.Name = "map3";
            this.map3.Size = new System.Drawing.Size(511, 515);
            this.map3.TabIndex = 10;
            this.map3.TabStop = false;
            // 
            // character
            // 
            this.character.Image = global::project.Properties.Resources.character;
            this.character.Location = new System.Drawing.Point(585, 358);
            this.character.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.character.Name = "character";
            this.character.Size = new System.Drawing.Size(59, 60);
            this.character.TabIndex = 4;
            this.character.TabStop = false;
            // 
            // ball
            // 
            this.ball.Image = global::project.Properties.Resources.Ball;
            this.ball.Location = new System.Drawing.Point(597, 291);
            this.ball.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.ball.Name = "ball";
            this.ball.Size = new System.Drawing.Size(59, 60);
            this.ball.TabIndex = 3;
            this.ball.TabStop = false;
            this.ball.Click += new System.EventHandler(this.ball_Click);
            // 
            // map2
            // 
            this.map2.Image = global::project.Properties.Resources.map2;
            this.map2.Location = new System.Drawing.Point(330, 31);
            this.map2.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.map2.Name = "map2";
            this.map2.Size = new System.Drawing.Size(511, 515);
            this.map2.TabIndex = 8;
            this.map2.TabStop = false;
            // 
            // map
            // 
            this.map.Image = global::project.Properties.Resources.map;
            this.map.Location = new System.Drawing.Point(379, 100);
            this.map.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.map.Name = "map";
            this.map.Size = new System.Drawing.Size(379, 336);
            this.map.TabIndex = 2;
            this.map.TabStop = false;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(66, 100);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(45, 15);
            this.label4.TabIndex = 11;
            this.label4.Text = "label4";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(1022, 96);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 12;
            this.button1.Text = "RESET";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(1022, 190);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 13;
            this.button2.Text = "NEXT";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1213, 688);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.character);
            this.Controls.Add(this.ball);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.map2);
            this.Controls.Add(this.map);
            this.Controls.Add(this.map3);
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            this.PreviewKeyDown += new System.Windows.Forms.PreviewKeyDownEventHandler(this.Form1_PreviewKeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.map3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.character)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ball)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.map2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.map)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox map;
        private System.Windows.Forms.PictureBox ball;
        public System.Windows.Forms.PictureBox character;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox map2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.PictureBox map3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
    }
}

