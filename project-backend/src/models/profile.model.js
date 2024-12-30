const { Schema, model } = require("mongoose");

const profileSchema = new Schema(
  {
    user: { type : Schema.Types.ObjectId, ref: "User", required: true },
    bio: { type : String },
    avatar: { type : String },
  },
  {
    timestamps: true,
  }
);

module.exports = model("Profile", profileSchema);
