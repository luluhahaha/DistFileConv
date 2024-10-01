The conversion tool is based on NREL Ditto tool. The original tool was for Cyme version 8 and we updated it and make it compatible to Cyme version 9. We improved the tool to convert multiple feeders simulateneously from a single set of cyme files. We have fixed issues in the conversion procee. The tool has been validated on real-world cyme feeders.

Two things need to be update based on user file:
1. Power source: the current version skip default and winter source, only read summer source
2. Load: check the load model for parsing load. 
Find the corresponding place in reader and update the ID based on the user's needs.