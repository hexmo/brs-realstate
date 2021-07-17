// Validators function callers
function validateLoginForm() {
	var email = document.forms['loginForm']['email'].value;
	var password = document.forms['loginForm']['password'].value;
	var emailHelp = document.getElementById('emailHelp');
	var passwordHelp = document.getElementById('passwordHelp');

	if (
		validateEmail(email, emailHelp) &&
		validatePassword(password, passwordHelp)
	) {
		return true;
	}

	return false;
}

function validateSignUpForm() {
	var name = document.forms['signUpForm']['name'].value;
	var phone = document.forms['signUpForm']['phone'].value;
	var email = document.forms['signUpForm']['email'].value;
	var password = document.forms['signUpForm']['password'].value;
	var nameHelp = document.getElementById('nameHelp');
	var phoneHelp = document.getElementById('phoneHelp');
	var emailHelp = document.getElementById('emailHelp');
	var passwordHelp = document.getElementById('passwordHelp');

	if (
		validateEmail(email, emailHelp) &&
		validatePassword(password, passwordHelp) &&
		validateName(name, nameHelp) &&
		validatePhone(phone, phoneHelp)
	) {
		return true;
	}

	return false;
}

// Validators functions
function validateEmail(email, emailHelp) {
	var mailformat = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-z]+';

	if (email == '') {
		emailHelp.innerHTML = "Email can't be empty.";
	} else if (!email.match(mailformat)) {
		emailHelp.innerHTML = 'Invalid email format.';
	} else {
		emailHelp.innerHTML = '';
		return true;
	}
	return false;
}

function validatePassword(password, passwordHelp) {
	var passwordFormat = '(?=.*[0-9])(?=.*[@#$%^&+=]).{8,}';
	if (password == '') {
		passwordHelp.innerHTML = "Password can't be empty.";
	} else if (password.length < 8) {
		passwordHelp.innerHTML = 'Password should be at least 8 characters long.';
	} else if (!password.match(passwordFormat)) {
		passwordHelp.innerHTML =
			'Password should contain at least one special character and a number.';
	} else {
		passwordHelp.innerHTML = '';
		return true;
	}

	return false;
}

function validateName(name, nameHelp) {
	if (name == '') {
		nameHelp.innerHTML = "Name can't be empty.";
	} else {
		nameHelp.innerHTML = '';
		return true;
	}

	return false;
}

function validatePhone(phone, phoneHelp) {
	if (phone == '') {
		phoneHelp.innerHTML = "Phone number can't be empty.";
	} else if (phone.length < 10) {
		phoneHelp.innerHTML = 'Phone number must be of 10 characters.';
	} else if (phone.substring(0, 2) != '98') {
		phoneHelp.innerHTML = 'Phone number should begin with 98****.';
	} else {
		phoneHelp.innerHTML = '';
		return true;
	}

	return false;
}
// Other utilities functions
function showPassword() {
	var password = document.getElementById('password');
	if (password.type === 'password') {
		password.type = 'text';
	} else {
		password.type = 'password';
	}
}
