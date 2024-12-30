const contacts = [
  {
    id: 1,
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "+1234567890",
  },
  {
    id: 2,
    name: "Jane Smith",
    email: "jane.smith@example.com",
    phone: "+9876543210",
  },

  {
    id: 3,
    name: "Mike Johnson",
    email: "mike.johnson@example.com",
    phone: "+1122334455",
  },
  {
    id: 4,
    name: "Alice Williams",
    email: "zlice.williams@example.com",
    phone: "+2233445566",
  },
];

const contact = (req, res) => {
  res.json(contacts);
};

const contactById = (req, res) => {
  const contactId = parseInt(req.params.id);
  const foundContact = contacts.find((cont) => cont.id === contactId);
  if (foundContact) {
    res.status(200).json({
      message: `This user is ${foundContact.name} with id of ${contactId}`,
    });
  } else {
    res.status(404).json({ message: "User not found" });
  }
};

const UpdateContactById = (req, res) => {
  const contact = parseInt(req.params.id);
  const { name, email, phone } = req.body;
  const foundContact = contacts.find((cont) => cont.id === contact);
  if (foundContact) {
    name ? (foundContact.name = name) : foundContact.name;
    email ? (foundContact.email = email) : foundContact.email;
    phone ? (foundContact.phone = phone) : foundContact.phone;
    res
      .status(200)
      .json({ message: `Contact updated successfully`, user: foundContact });
  } else {
    res.status(404).json({ message: "User not found" });
  }
};

const deleteUserById = (req, res) => {
  const contact = parseInt(req.params.id);
  const index = contacts.findIndex((cont) => cont.id === contact);
  if (index !== -1) {
    contacts.splice(index, 1);
    res.status(200).json({ message: `User deleted successfully` });
  } else {
    res.status(404).json({ message: "User not found" });
  }
};

const addContact = (req, res) => {
  const body = req.body;
  const { name, email, phone } = req.body;
  const user = { id: generateId(), ...body };
  const exisitingUser = contacts.find(
    (user) => user.name == name || user.email == email
  );
  if (exisitingUser) {
    res.json({ message: "User aready exist" });
  } else {
    contacts.push(user);
    res.json({ message: "User succesfully added", user: user });
  }
};

function generateId() {
  return contacts[contacts.length - 1].id + 1;
}

const sortAllContact = (req, res) => {
  const sortBy = req.params.sortBy;

  const sortedContacts = contacts.sort((a, b) =>
    a[sortBy].localeCompare(b[sortBy])
  );
  res.json(sortedContacts);
};

module.exports = {
  contact,
  contactById,
  UpdateContactById,
  deleteUserById,
  sortAllContact,
  addContact,
};
