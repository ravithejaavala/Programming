package main

import (
	"fmt"
	"strings"
)

// These are package variables, these are not defined using ":=" this type
//
//2:28 min
var confName = "Go-Lang Conference"

const confTickets = 50

var remainTickets = 50

var names []string
var emails []string
var notickets []int

func main() {
	//var confName = "Go-Lang Conference"
	//const confTickets = 50            ----------these are defineed outside the function
	//var remainTickets = 50

	// data type is auto matically identified by Go, while declaring the value of it
	// confName := "Go-Lang Conference" insted of above we can use this i.e with out declaring the var and data type
	// we can use "%T" to find the data type in the Printf()
	// we can't use the above to declare  "const"

	// in "Printf(), Println()" in these functions "P" should be in captial

	//fmt.Printf("Welcome to %v Booking Application\n", confName)
	//fmt.Printf("We have total of %v tickets ,Now the available tickets are %v\n", confTickets, remainTickets)
	//fmt.Printf("Buy your tickets to attend %v\n", confName)

	//above 3 statements are executed in the below "greetusers()" fuction
	greetusers()

	//var names []string
	//var emails []string      ----these are defined outside the function
	//var notickets []int

	// Above is the empty slice (size is not defines), with type string, we can add any number of elements to it by using "names=append(names, ----element you want to add----)"
	//var names [50]string
	// Above is the decleration of an empty array, with size of 50 elements and string data type
	// || var userNames = [50] string {"Ravi", "teja", "Reddy"} || this line is to declare the list of some elements with data type string and size of 50 elements

	for {
		// Function is defined to take inputs from the user
		userfname, userlname, userEmail, userTickets := userinputs() //this can't define outside the function, because it need to iterate
		// function is defined to validate the user inputs and returning multiple values from that function
		isValidname, isValidemail, isValidtickets := validateuser(userfname, userlname, userEmail, userTickets) //this can't define outside the function, because it need to iterate
		// Also we are declaring multiple variables at a time
		if isValidemail && isValidname && isValidtickets {
			bookticket(userfname, userlname, userEmail, userTickets)

			if remainTickets == 0 {
				fmt.Printf("!!!!!!! All tickets are sold out !!!!!!!!!!!!\n")
				fmt.Printf("Comeback next year to Attend the conference")
				break
			}
		} else { // 'else if' is used for more conditions
			if !isValidname {
				fmt.Printf("You entered First name or Last name is too short\n")
			}
			if !isValidemail {
				fmt.Printf("You entered Email doesn't contain '@'\n")
			}
			if !isValidtickets {
				fmt.Printf("You entered NO.of Tickets is invalid\n")
			}
			// we are using '!' symbol to check True or false correctly, if validate is true(correct), then dont need to execute that
			// Here we used only if statements, because we need to check all the conditions
		}

	}
}

func userinputs() (string, string, string, int) {
	var userfname string
	var userlname string
	var userEmail string
	//var userCity string

	// But here we need to menction the data type, because we are not assigning any value to it
	var userTickets int

	fmt.Print("Enter your first name : ")
	fmt.Scan(&userfname)

	fmt.Print("Enter your last name : ")
	fmt.Scan(&userlname)

	fmt.Print("Enter your Email ID : ")
	fmt.Scan(&userEmail)

	fmt.Print("Enter the no.of Tickets you want : ")
	fmt.Scan(&userTickets)

	//fmt.Print("Enter the City you want to attend : ")
	//fmt.Scan(&userCity)

	return userfname, userlname, userEmail, userTickets
}

func getfirstnames() []string {
	// Here "[]string" with in the brackets define's the input parameter, while "[]string" out side the brackets define's the output(return) parameter
	var firstnames []string
	for _, first := range names { // "_" is used as Blank Identifier, this is used to say thet thers is no variable here, insted of leaving blank
		var name = strings.Fields(first)
		firstnames = append(firstnames, name[0])
	}
	return firstnames //define of both input and output(return) parameterswith types are compulsary when they are used
}

func bookticket(userfname string, userlname string, userEmail string, userTickets int) {

	names = append(names, userfname+" "+userlname)
	emails = append(emails, userEmail)
	notickets = append(notickets, userTickets)
	remainTickets = remainTickets - userTickets
	// Here function is defined to print first names of the user's
	firstNames := getfirstnames()
	fmt.Printf("First names of the users :%v\n", firstNames)
	fmt.Printf("Thank you %v, for booking %v Tickets, you will receive a conformation Email for %v\n", userfname+" "+userlname, userTickets, userEmail)
	fmt.Printf("%v tickets are remaining in our conference, from total of %v Tickets", remainTickets, confTickets)
	fmt.Printf("These are our bookings : \nNames-- %v\nEmails-- %v\nTickets-- %v\n", names, emails, notickets)

}

/*
-------------------- "switch" Statement --------------------
city := "London"

switch city {
	case "New york":
		//Execute code to book tickets in New york city
	case "Singapure":
		//Execute code to book tickets in Singapure city
	case "London", "Berlin": // used to check multiple conditions
		//Execute code to book tickets in London city
	case "Hyderabad":
		//Execute code to book tickets in Hyderabad city
	default : // if no matches are found, then default case executes
		fmt.Print("Invalid City")
} */
