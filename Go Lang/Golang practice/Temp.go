package main

// "go mod init --file name--" to initalise 'go.mod' file, then only the go files are able to run
import (
	"fmt"
	"strings"
)

func main() {
	var names = [2]string{"Ravi Reddy", "Teja Reddy"}
	var firstnames []string
	for _, first := range names {
		var name = strings.Fields(first)
		firstnames = append(firstnames, name[0])
	}
	fmt.Printf("First names of the users : %v", firstnames)
}
