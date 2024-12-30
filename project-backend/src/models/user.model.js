const { Schema, model } = require("mongoose");
const userSchema = new Schema(
  {
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    password: { type: String },
    googleId: { type: String }, 
    authMethod: {
      type: String,
      enum: ['local', 'google'], 
      default: 'local'
    },
    plan: {
      type: String,
      enum: ['free', 'professional', 'enterpris'],
      default: 'free'
    }
  },
  {
    timestamps: true,
  }
);

module.exports = model("User", userSchema);
